import polars as pl

# Created by Koen Vossen, 
# Github: https://github.com/koenvo
# Twitter/x Handle: https://twitter.com/mr_le_fox
# https://x.com/mr_le_fox/status/1741893400947839362?s=20
def create_polars_df():
    pl.Config.set_streaming_chunk_size(4_000_000)
    return (
        pl.scan_csv(
            "data/generated/medicoes_1000000000.txt",
            separator=";",
            has_header=False,
            new_columns=["station", "temperature"],  # match your usage
            schema_overrides={"station": pl.Utf8, "temperature": pl.Float64}  # new param name
        )
        .group_by("station")
        .agg([
            pl.col("temperature").max().alias("max"),
            pl.col("temperature").min().alias("min"),
            pl.col("temperature").mean().alias("mean"),
        ])
        .sort("station")
        .collect(engine="streaming")
    )

if __name__ == "__main__":
    import time

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()
    df = create_polars_df()
    took = time.time() - start_time
    print(df)
    print(f"Polars Took: {took:.2f} sec")