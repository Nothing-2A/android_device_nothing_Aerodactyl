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
#if 0
using ::aidl::vendor::mediatek::hardware::pq_aidl::IPictureQuality_AIDL;
#endif

int main() {
    ABinderProcess_setThreadPoolMaxThreadCount(0);

#if 0
    std::shared_ptr<IPictureQuality_AIDL> pqService = ndk::SharedRefBase::make<IPictureQuality_AIDL>();

    const std::string pqInstance = std::string() + IPictureQuality_AIDL::descriptor + "/default";
    binder_status_t pqStatus = AServiceManager_addService(pqService->asBinder().get(), pqInstance.c_str());
    CHECK(pqStatus == STATUS_OK);
#endif

    std::shared_ptr<Fingerprint> fingerprint = ndk::SharedRefBase::make<Fingerprint>();

    const std::string instance = std::string() + Fingerprint::descriptor + "/default";
    binder_status_t status = AServiceManager_addService(fingerprint->asBinder().get(), instance.c_str());
    CHECK(status == STATUS_OK);

    ABinderProcess_joinThreadPool();
    return EXIT_FAILURE; // should not reach
}
