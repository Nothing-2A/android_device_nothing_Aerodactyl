/*
 * Copyright (C) 2024 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "Fingerprint.h"

#include <android/binder_manager.h>
#include <android/binder_process.h>
#include <android-base/logging.h>

using ::aidl::android::hardware::biometrics::fingerprint::Fingerprint;
using ::aidl::vendor::mediatek::hardware::pq_aidl::IPictureQuality_AIDL;

int main() {
    ABinderProcess_setThreadPoolMaxThreadCount(0);

    const std::string instance = std::string() + IPictureQuality_AIDL::descriptor + "/default";
    std::shared_ptr<IPictureQuality_AIDL> pictureQuality = IPictureQuality_AIDL::fromBinder(
            ndk::SpAIBinder(AServiceManager_waitForService(instance.c_str())));

    std::shared_ptr<Fingerprint> fingerprint = ndk::SharedRefBase::make<Fingerprint>(pictureQuality);

    const std::string instance = std::string() + Fingerprint::descriptor + "/default";
    binder_status_t status = AServiceManager_addService(fingerprint->asBinder().get(), instance.c_str());
    CHECK(status == STATUS_OK);

    ABinderProcess_joinThreadPool();
    return EXIT_FAILURE; // should not reach
}
