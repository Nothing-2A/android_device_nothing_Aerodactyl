/*
 * Copyright (C) 2025 The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

package org.lineageos.felica

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log

class BootCompletedReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        Log.d(TAG, "Received boot completed intent")
        FelicaDisabler.enableOrDisableFelica(context)
    }

    companion object {
        private const val TAG = "NothingFelicaBootReceiver"
    }
}
