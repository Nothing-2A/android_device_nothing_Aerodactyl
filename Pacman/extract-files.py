#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/nothing/Aerodactyl',
]

module = ExtractUtilsModule(
    'Pacman',
    'nothing',
    device_rel_path='device/nothing/Aerodactyl/Pacman',
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'Aerodactyl', module.vendor)
    utils.run()
