from pybwtool import extract, extract_mean
import pytest

def test_extract():
    extract("tests/HepG2.bed", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract("tests/HALLO.bed", "tests/ENCFF523IAP.bigWig")

def test_extract_mean():
    extract_mean("tests/HepG2.bed", "tests/ENCFF523IAP.bigWig")
    with pytest.raises(ValueError):
        extract("tests/HepG2.bed", "tests/GALLO.bigWig")