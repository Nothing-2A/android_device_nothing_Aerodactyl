#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# A/B
$(call inherit-product, $(SRC_TARGET_DIR)/product/virtual_ab_ota/launch_with_vendor_ramdisk.mk)

AB_OTA_POSTINSTALL_CONFIG += \
    RUN_POSTINSTALL_system=true \
    POSTINSTALL_PATH_system=system/bin/otapreopt_script \
    FILESYSTEM_TYPE_system=ext4 \
    POSTINSTALL_OPTIONAL_system=true

AB_OTA_POSTINSTALL_CONFIG += \
    RUN_POSTINSTALL_vendor=true \
    POSTINSTALL_PATH_vendor=bin/checkpoint_gc \
    FILESYSTEM_TYPE_vendor=ext4 \
    POSTINSTALL_OPTIONAL_vendor=true

PRODUCT_PACKAGES += \
    com.android.hardware.boot \
    android.hardware.boot-service.default_recovery

PRODUCT_PACKAGES += \
    create_pl_dev \
    create_pl_dev.recovery

PRODUCT_PACKAGES += \
    checkpoint_gc \
    otapreopt_script \
    update_engine \
    update_engine_sideload \
    update_verifier

# API
BOARD_SHIPPING_API_LEVEL := 33
PRODUCT_SHIPPING_API_LEVEL := 34

# Audio
PRODUCT_PACKAGES += \
    android.hardware.audio.effect@7.0-impl \
    android.hardware.audio.service \
    android.hardware.bluetooth.audio-impl \
    android.hardware.soundtrigger@2.3-impl

PRODUCT_PACKAGES += \
    audio.primary.default \
    audio.bluetooth.default \
    audio.r_submix.default \
    audio.usb.default

# Boot animation
TARGET_SCREEN_HEIGHT := 2412
TARGET_SCREEN_WIDTH := 1080

# Characteristics
PRODUCT_CHARACTERISTICS := nosdcard

# Display
PRODUCT_PACKAGES += \
    android.hardware.memtrack-service.mediatek-mali

# DRM
PRODUCT_PACKAGES += \
    android.hardware.drm-service.clearkey

# Enforce generic ramdisk allow list
$(call inherit-product, $(SRC_TARGET_DIR)/product/generic_ramdisk.mk)

# Enable project quotas and casefolding for emulated storage without sdcardfs
$(call inherit-product, $(SRC_TARGET_DIR)/product/emulated_storage.mk)

# Gatekeeper
PRODUCT_PACKAGES += \
    android.hardware.gatekeeper@1.0-impl \
    android.hardware.gatekeeper@1.0-service

# Health
PRODUCT_PACKAGES += \
    android.hardware.health-service.mediatek \
    android.hardware.health-service.mediatek-recovery

# Init
PRODUCT_PACKAGES += \
    fstab.mt6886 \
    fstab.mt6886.vendor_ramdisk

PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/init/init.recovery.mt6886.rc:$(TARGET_COPY_OUT_RECOVERY)/root/init.recovery.mt6886.rc

# NFC
PRODUCT_PACKAGES += \
    android.hardware.nfc-service.st \
    android.hardware.secure_element@1.2-service-gto

PRODUCT_PACKAGES += \
    com.android.nfc_extras \
    SecureElement \
    Tag

# Partitions
PRODUCT_USE_DYNAMIC_PARTITIONS := true

PRODUCT_PACKAGES += \
    android.hardware.fastboot@1.1-impl.custom \
    fastbootd

# Screen density
PRODUCT_AAPT_CONFIG := normal
PRODUCT_AAPT_PREF_CONFIG := xxhdpi

# Sensors
PRODUCT_PACKAGES += \
    android.hardware.sensors-service.multihal

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH) \
	hardware/mediatek

# Thermal
PRODUCT_PACKAGES += \
    android.hardware.thermal@1.0-impl

# USB
PRODUCT_PACKAGES += \
    android.hardware.usb-service.mediatek \
    android.hardware.usb.gadget-service.mediatek

# Vibrator
$(call soong_config_set, vibrator, vibratortargets, vibratoraidlV2target)

PRODUCT_PACKAGES += \
    vendor.qti.hardware.vibrator.service

PRODUCT_COPY_FILES += \
    vendor/qcom/opensource/vibrator/excluded-input-devices.xml:$(TARGET_COPY_OUT_VENDOR)/etc/excluded-input-devices.xml

# VNDK
PRODUCT_PACKAGES += \
    vndservicemanager

# Wifi
PRODUCT_PACKAGES += \
    wpa_supplicant \
    hostapd \
    android.hardware.wifi-service

# Inherit the proprietary files
$(call inherit-product, vendor/nothing/Pacman/Pacman-vendor.mk)
