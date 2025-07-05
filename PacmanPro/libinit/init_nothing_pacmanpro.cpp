/*
 * Copyright (C) 2021-2025 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_variant.h>

#include "vendor_init.h"

static const variant_info_t PacmanProEEA_info = {
    .sku_value = "EEA",

    .name = "PacmanProEEA",
    .build_fingerprint = "Nothing/PacmanProEEA/PacmanPro:15/AP3A.240905.015.A2/2504101524:user/release-keys",
};

static const variant_info_t PacmanProIND_info = {
    .sku_value = "IND",

    .name = "PacmanProIND",
    .build_fingerprint = "Nothing/PacmanProIND/PacmanPro:15/AP3A.240905.015.A2/2504101524:user/release-keys",
};

static const variant_info_t PacmanProJPN_info = {
    .sku_value = "JPN",

    .name = "PacmanProJPN",
    .build_fingerprint = "Nothing/PacmanProJPN/PacmanPro:15/AP3A.240905.015.A2/2504101524:user/release-keys",
};

static const variant_info_t PacmanPro_info = {
    .sku_value = "",

    .name = "PacmanPro",
    .build_fingerprint = "Nothing/PacmanPro/PacmanPro:15/AP3A.240905.015.A2/2504101524:user/release-keys",
};

static const std::vector<variant_info_t> variants = {
    PacmanProEEA_info,
    PacmanProIND_info,
    PacmanProJPN_info,
    PacmanPro_info,
};

void vendor_load_properties() {
    search_variant(variants);
}
