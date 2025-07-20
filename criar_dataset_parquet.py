import os
import random
import time
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def construir_lista_estacoes_meteorologicas():
    """
    Obtém os nomes das estações meteorológicas a partir de um arquivo e remove duplicatas.
    """
    with open('./data/amostra_44k.csv', 'r', encoding="utf-8") as arquivo:
        return list(set(linha.split(';')[0] for linha in arquivo if "#" not in linha))


def converter_bytes(num):
    """
    Converte bytes para um formato legível (ex: KB, MB, GB).
    """
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if num < 1024:
            return f"{num:.1f} {unidade}"
        num /= 1024


def formatar_tempo_decorrido(segundos):
    """
    Formata o tempo decorrido de forma simplificada.
    """
    minutos, segundos = divmod(segundos, 60)
    return f"{int(minutos)}m {int(segundos)}s" if minutos else f"{segundos:.2f}s"


def calcular_tamanho_pasta(path):
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total

def gerar_dados_teste(num_registros):
    """
    Gera e salva um arquivo Parquet com medições sintéticas de temperatura.
    """
    inicio_tempo = time.time()
    nomes_estacoes = construir_lista_estacoes_meteorologicas()
    estacoes_10k_max = random.choices(nomes_estacoes, k=10_000)
    
    # Caminho de saída para Parquet
    arquivo_saida = f"./data/generated/medicoes_{num_registros}.parquet"
    tamanho_lote = 10_000  # Processamento em lotes
    lote_dados = []

    print(f"Criando {arquivo_saida}...")

    try:
        for _ in range(num_registros // tamanho_lote):
            lote = random.choices(estacoes_10k_max, k=tamanho_lote)
            lote_dados.extend([(estacao, round(random.uniform(-99.9, 99.9), 1)) for estacao in lote])

            # Salvar em lotes para evitar consumo excessivo de memória
            if len(lote_dados) >= 40_000_000:
                salvar_parquet(lote_dados, arquivo_saida)
                lote_dados = []  # Limpa a lista para o próximo lote

        # Salvar qualquer dado restante
        if lote_dados:
            salvar_parquet(lote_dados, arquivo_saida)

        # Verifica o tamanho do arquivo gerado
        tamanho_arquivo = calcular_tamanho_pasta(arquivo_saida)
        print(f"Arquivo Parquet gerado: {arquivo_saida}")
        print(f"Tamanho final: {converter_bytes(tamanho_arquivo)}")
        print(f"Tempo decorrido: {formatar_tempo_decorrido(time.time() - inicio_tempo)}")
    
    except Exception as e:
        print("Erro ao criar o arquivo Parquet:", e)


# def salvar_parquet(lote_dados, arquivo_saida):
#     """
#     Salva um lote de dados no formato Parquet.
#     """
#     df = pd.DataFrame(lote_dados, columns=["station", "temperature"])
#     table = pa.Table.from_pandas(df)

#     # Salvar no formato Parquet com Append (salva em múltiplos arquivos)
#     pq.write_to_dataset(table, root_path=arquivo_saida, filesystem=None)

def salvar_parquet(lote_dados, arquivo_saida):
    df = pd.DataFrame(lote_dados, columns=["station", "temperature"])

    # Pegue todas estações únicas no batch atual
    estações_unicas = df["station"].unique()
    
    # Defina um tamanho máximo de estações por batch para evitar ultrapassar limite
    max_estacoes_por_batch = 1000

    for i in range(0, len(estações_unicas), max_estacoes_por_batch):
        grupo_estacoes = estações_unicas[i:i + max_estacoes_por_batch]
        df_grupo = df[df["station"].isin(grupo_estacoes)]
        table = pa.Table.from_pandas(df_grupo, preserve_index=False)
        
        pq.write_to_dataset(
            table,
            root_path=arquivo_saida,
            partition_cols=["station"],
            max_partitions=10240  # só para garantir que o limite seja maior
        )


if __name__ == "__main__":
    num_registros = 1_000_000_002  # Número de registros parametrizado
    gerar_dados_teste(num_registros)
