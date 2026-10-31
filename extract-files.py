#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.file import File
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/nothing/Aerodactyl',
    'hardware/mediatek',
    'hardware/mediatek/libion_mtk',
    'hardware/mediatek/libmtkperf_client',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'vendor.mediatek.hardware.videotelephony-V1-ndk'
    ): lib_fixup_vendor_suffix,
}


_displayservice_ping = (
    b'_ZN7lineage10frameworks14displayservice4V1_014IEventCallback4pingEv'
)
_displayservice_unresolved = (
    rb'_ZN7lineage10frameworks14displayservice4V1_01[45]I[A-Za-z0-9_]*'
    rb'(?:linkToDeath|unlinkToDeath|getDebugInfo|getHashChain|'
    rb'interfaceChain|interfaceDescriptor|5debug|registerForNotifications)'
    rb'[A-Za-z0-9_]*'
)
_displayservice_ctor_vtable = (
    rb'_ZTCN[A-Za-z0-9_]+E\d+_'
    rb'N7lineage10frameworks14displayservice4V1_01[45]I[A-Za-z0-9_]*E'
)


blob_fixups: blob_fixups_user_type = {
    'system_ext/etc/init/init.vtservice.rc': blob_fixup()
        .regex_replace('start', 'enable'),
    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),
    'system_ext/priv-app/ImsService/ImsService.apk': blob_fixup()
        .apktool_patch('blob-patches/ImsService'),
    (
        'vendor/bin/hw/mt6886/android.hardware.graphics.allocator-V2-service-mediatek.mt6886',
        'vendor/lib64/hw/mt6886/android.hardware.graphics.allocator-V2-mediatek.so',
        'vendor/lib64/hw/mt6886/mapper.mediatek.so',
        'vendor/lib64/libcodec2_fsr.so',
        'vendor/lib64/libcodec2_vpp_AIMEMC_plugin.so',
        'vendor/lib64/libcodec2_vpp_AISR_plugin.so',
        'vendor/lib64/libgpud.so',
        'vendor/lib64/vendor.mediatek.hardware.camera.isphal-V1-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V7-ndk.so'
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V6-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
    'vendor/bin/hw/mt6886/camerahalserver': blob_fixup()
        .add_needed('libcamera_metadata_shim.so'),
    'vendor/bin/mnld' : blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so')
        .replace_needed('libmnl.so', 'libmnl_mtk.so'),
    'vendor/etc/displayconfig/display_id_4627039422300187648.xml': blob_fixup()
        .regex_replace('<transitionPoint>0.6</transitionPoint>', '<transitionPoint>0.9221</transitionPoint>'),
    (
        'vendor/etc/libnfc-hal-st.conf',
        'vendor/etc/libnfc-hal-st-st54j.conf'
    ): blob_fixup()
        .regex_replace('# STNFC_FW_BIN_NAME', 'STNFC_FW_BIN_NAME')
        .regex_replace('# STNFC_FW_CONF_NAME', 'STNFC_FW_CONF_NAME')
        .regex_replace('STNFC_FW_DEBUG_ENABLED=1', 'STNFC_FW_DEBUG_ENABLED=0'),
    'vendor/lib64/hw/mt6886/vendor.mediatek.hardware.pq_aidl-impl.so': blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v36.so'),
    'vendor/lib64/hw/audio.primary.mediatek.so': blob_fixup()
        .replace_needed('android.hardware.audio.effect-V2-ndk.so', 'android.hardware.audio.effect-V3-ndk.so')
        .replace_needed('android.hardware.bluetooth.audio-V4-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v36.so')
        .replace_needed('vendor.mediatek.hardware.bluetooth.audio-V1-ndk.so', 'vendor.mediatek.hardware.bluetooth.audio-V4-ndk.so'),
    'vendor/lib64/hw/android.hardware.audio.effect.aidl-impl-mediatek.so': blob_fixup()
        .replace_needed('libaudio_aidl_conversion_common_ndk.so', 'libaudio_aidl_conversion_common_ndk_prebuilt.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v36.so'),
    (
        'vendor/bin/hw/android.hardware.audio.service-aidl.mediatek',
        'vendor/lib64/hw/android.hardware.soundtrigger3-impl.so',
        'vendor/lib64/soundfx/libdiraceffect_NTaidl.so',
        'vendor/lib64/soundfx/libspatializeraidl.so'
    ): blob_fixup()
        .replace_needed('libaudio_aidl_conversion_common_ndk.so', 'libaudio_aidl_conversion_common_ndk_prebuilt.so'),
    'vendor/lib64/hw/hwcomposer.mtk_common.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V6-ndk.so', 'android.hardware.graphics.common-V7-ndk.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v36.so'),
    'vendor/lib64/mt6886/libmorpho_video_stabilizer.so': blob_fixup()
        .add_needed('libutils.so'),
    (
        'vendor/lib64/mt6886/libmtkcam_grallocutils.so',
        'vendor/lib64/mt6886/libmtkcam_grallocutils_aidlv2helper.so'
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V5-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
    'vendor/lib64/mt6886/libmtkcam_hal_aidl_common.so': blob_fixup()
        .replace_needed('android.hardware.camera.common-V2-ndk.so', 'android.hardware.camera.common-V1-ndk.so'),
    'vendor/lib64/mt6886/libmtkcam_hal_android_app_cbadaptor.so': blob_fixup()
        .replace_needed('android.frameworks.displayservice@1.0.so',
                        'lineage.frameworks.displayservice@1.0.so')
        .binary_regex_replace(
            b'7android10frameworks14displayservice',
            b'7lineage10frameworks14displayservice')
        .binary_regex_replace(
            _displayservice_unresolved,
            lambda m: _displayservice_ping.ljust(len(m.group(0)), b'\x00'))
        .binary_regex_replace(
            _displayservice_ctor_vtable,
            lambda m: _displayservice_ping.ljust(len(m.group(0)), b'\x00')),
    'vendor/lib64/android.hardware.audio.core-impl-mediatek.so': blob_fixup()
        .add_needed('libaudioutils_shim.so')
        .replace_needed('libaudio_aidl_conversion_common_ndk.so', 'libaudio_aidl_conversion_common_ndk_prebuilt.so'),
    (
        'vendor/lib64/android.hardware.bluetooth.audio-impl-mediatek.so',
        'vendor/lib64/libbluetooth_audio_session_aidl_mtk.so'
    ): blob_fixup()
        .replace_needed('vendor.mediatek.hardware.bluetooth.audio-V1-ndk.so', 'vendor.mediatek.hardware.bluetooth.audio-V4-ndk.so'),
    (
        'vendor/lib64/libcodec2_mtk_vdec.so',
        'vendor/lib64/libcodec2_mtk_venc.so'
    ): blob_fixup()
        .replace_needed('libformatter.so', 'libformatter_mtk.so'),
    (
        'vendor/lib64/libpqxmlflagparser.so',
        'vendor/lib64/libpqxmlparser.so',
        'vendor/lib64/librt_extamp_intf.so',
        'vendor/lib64/libsilkybrightnesscore.so',
        'vendor/lib64/mt6886/libmmlpqImpl.so'
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v36.so'),
    'vendor/lib64/libstfaceunlockppl.so': blob_fixup()
        .sig_replace('fd 7b bd a9 fd 03 00 91 f3 53 01 a9 f4 03 00 aa f3 03 01 aa a0 6e 02 d0', '00 00 80 52 c0 03 5f d6 1f 20 03 d5 1f 20 03 d5 1f 20 03 d5 1f 20 03 d5')
        .sig_replace('fd 7b bb a9 fd 03 00 91 f3 53 01 a9 a0 17 00 f9 5b c3 ff 97 a1 17 40 f9', '00 00 80 52 c0 03 5f d6 1f 20 03 d5 1f 20 03 d5 1f 20 03 d5 1f 20 03 d5')
        .sig_replace('61 75 02 f0 21 80 66 39 01 00 00 b9 00 00 80 52 c0 03 5f d6', '21 00 80 52 01 00 00 b9 00 00 80 52 c0 03 5f d6 1f 20 03 d5'),
}  # fmt: skip

module = ExtractUtilsModule(
    'Aerodactyl',
    'nothing',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
