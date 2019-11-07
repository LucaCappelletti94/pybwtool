from pybwtool import extract, extract_mean, extract_max
import pytest


def test_extract():
    extract("tests/HepG2.bed", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract("tests/HALLO.bed", "tests/ENCFF523IAP.bigWig")


def test_extract_mean():
    extract_mean("tests/HepG2.bed", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract_mean("tests/HepG2.bed", "tests/GALLO.bigWig")


def test_extract_max():
    extract_max("tests/HepG2.bed", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract_max("tests/HepG2.bed", "tests/GALLO.bigWig")
