# -*- coding: utf-8; Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# This file is part of FATSLiM --- http://fatslim.github.io/
#
# Copyright (c) 2013-2018, Sébastien Buchoux
# Copyright (c) 2019, by the FATSLiM development team (see AUTHORS file)
#
# FATSLiM is free software and is released under the GNU Public Licence,
# v3 or any higher version
#
# If you use FATSLiM in publised work, please cite:
#
# S. Buchoux.
# FATSLiM: a fast and robust software to analyze MD simulations of membranes.
# Bioinformatics 33(1) (2017), 133--134, doi:10.1093/bioinformatics/btw563
#

# Global imports
import pytest
import MDAnalysis as mda

# Local imports
from .data import MODEL_FLAT_GRO, MODEL_VESICLE_GRO
from ..coreobjects import LipidSystem


@pytest.fixture(scope="session")
def universe_model_flat() -> mda.Universe:
    u = mda.Universe(MODEL_FLAT_GRO)
    return u


@pytest.fixture(scope="session")
def system_model_flat() -> LipidSystem:
    u = mda.Universe(MODEL_FLAT_GRO)
    system = LipidSystem(u, "name PO4")
    return system


@pytest.fixture(scope="session")
def system_model_vesicle() -> LipidSystem:
    u = mda.Universe(MODEL_VESICLE_GRO)
    system = LipidSystem(u, "name PO4")
    return system