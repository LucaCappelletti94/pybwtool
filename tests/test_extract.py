import os
import pandas as pd
from pybwtool import extract
import pytest


def test_extract():
    df = extract(
        bed_path="tests/HepG2.bed",
        bigwig_path="tests/ENCFF523IAP.bigWig"
    )
    path = "{pwd}/expected/test.bed".format(
        pwd=os.path.dirname(os.path.abspath(__file__))
    )
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
    csv1 = pd.read_csv("maybe.bed", sep="\t")

    extract(
        bed_path="tests/HepG2.bed",
        bigwig_path="tests/ENCFF523IAP.bigWig",
        target="maybe.bed"
    )

    csv2 = pd.read_csv("maybe.bed", sep="\t")

    pd.testing.assert_frame_equal(
        csv1,
        csv2
    )

def test_extract_to_compressed():
    extract(
        bed_path="tests/HepG2.bed",
        bigwig_path="tests/ENCFF523IAP.bigWig",
        target="maybe.bed.gz"
    )
    csv1 = pd.read_csv("maybe.bed.gz", sep="\t")

    extract(
        bed_path="tests/HepG2.bed",
        bigwig_path="tests/ENCFF523IAP.bigWig",
        target="maybe.bed.gz"
    )

    csv2 = pd.read_csv("maybe.bed.gz", sep="\t")

    pd.testing.assert_frame_equal(
        csv1,
        csv2
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
