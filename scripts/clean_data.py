"""
Simple data cleaning helper for Amazon Prime EDA
Usage:
    python scripts/clean_data.py --input path/to/raw.csv --output data/cleaned.csv

The script performs minimal cleaning: drops empty columns, strips whitespace
from string columns, normalizes column names, parses numeric rating fields,
and extracts primary genre when multiple genres are present.
"""
import argparse
import pandas as pd
import numpy as np


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    return df


def parse_numeric(df: pd.DataFrame, cols):
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    return df


def extract_primary_genre(df: pd.DataFrame, genre_col='genres'):
    if genre_col in df.columns:
        df['primary_genre'] = (
            df[genre_col].fillna('')
            .astype(str)
            .apply(lambda s: s.split(',')[0].strip() if s else np.nan)
        )
    return df


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)
    # Drop completely empty columns
    df = df.dropna(axis=1, how='all')
    # Strip whitespace from object columns
    obj_cols = df.select_dtypes(include=['object']).columns
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip()
        df[c] = df[c].replace({'': pd.NA})
    # Parse some common numeric fields
    df = parse_numeric(df, ['imdb_score', 'tmdb_score', 'popularity', 'vote_count'])
    # Extract primary genre if provided under various possible column names
    if 'genres' in df.columns:
        df = extract_primary_genre(df, 'genres')
    elif 'genre' in df.columns:
        df = extract_primary_genre(df, 'genre')
    # Normalize release year if possible
    if 'release_year' in df.columns:
        df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64')
    return df


def main():
    parser = argparse.ArgumentParser(description='Clean raw Amazon Prime CSV')
    parser.add_argument('--input', '-i', required=True, help='Path to raw CSV')
    parser.add_argument('--output', '-o', default='data/cleaned.csv', help='Path to cleaned CSV output')
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    cleaned = basic_clean(df)
    cleaned.to_csv(args.output, index=False)
    print(f'Wrote cleaned data to {args.output}')


if __name__ == '__main__':
    main()
