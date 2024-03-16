# -*- coding: utf-8 -*-

import os

from PyPDFForm import FormWrapper


def test_ds82(existed_pdf_directory, pdf_samples, request):
    expected_path = os.path.join(pdf_samples, "simple", "scenario", "existed", "DS82_expected.pdf")
    with open(expected_path, "rb+") as f:
        obj = FormWrapper(os.path.join(existed_pdf_directory, "DS82.pdf")).fill(
            {
                "LastName": "Smith",
            }
        )

        request.config.results["expected_path"] = expected_path
        request.config.results["stream"] = obj.read()

        expected = f.read()

        assert len(obj.read()) == len(expected)
        assert obj.stream == expected
