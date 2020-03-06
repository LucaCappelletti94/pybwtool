import os
import pandas as pd
from pybwtool import extract
import pytest


def test_extract():
    bed, scores = extract(
        bed_path="tests/HepG2.bed",
        bigwig_path="tests/ENCFF523IAP.bigWig"
    )
    path = "{pwd}/expected/test.bed".format(
        pwd=os.path.dirname(os.path.abspath(__file__))
    )
    scores.columns = [
        str(col)
        for col in scores.columns
    ]
    df = pd.concat([
        bed, scores
    ], axis=1)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        df.to_csv(path)
    pd.testing.assert_frame_equal(
        pd.read_csv(path, index_col=0),
        df,
        check_names=False
    )

def test_extract_to_file():
    extract(
        bed_path="tests/HepG2.bed",
        bigwig_path="tests/ENCFF523IAP.bigWig",
        target="maybe.bed"
    )


def test_wrong_parameters():
    with pytest.raises(ValueError):
        extract("tests/HALLO.bed", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract("tests/HepG2_header.bed", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract("tests/HepG2.csv", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract("tests/HepG2_small.bed", "tests/ENCFF523IAP.bigWig")
