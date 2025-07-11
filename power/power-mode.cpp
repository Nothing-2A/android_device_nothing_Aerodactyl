/*
 * SPDX-FileCopyrightText: The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

#include <aidl/android/hardware/power/BnPower.h>

#include <android-base/file.h>
#include <android-base/logging.h>

using ::aidl::android::hardware::power::Mode;

namespace aidl::google::hardware::power::impl::pixel {

bool isDeviceSpecificModeSupported(Mode type, bool* _aidl_return) {
    switch (type) {
        case Mode::DOUBLE_TAP_TO_WAKE:
            *_aidl_return = true;
            return true;
        default:
            return false;
    }
}

bool setDeviceSpecificMode(Mode type, bool enabled) {
    switch (type) {
        case Mode::DOUBLE_TAP_TO_WAKE: {
            LOG(INFO) << "Power mode: " << toString(type) << " isDoubleTapEnabled: " << enabled;

            ::android::base::WriteStringToFile(enabled ? "1" : "0", "/sys/devices/platform/soc/11013000.spi3/spi_master/spi3/spi3.0/fts_gesture_mode");

            return true;
        }
        default:
            return false;
    }
}

}  // namespace
