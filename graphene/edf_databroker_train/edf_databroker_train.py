# Copyright (C) 2021 The AURA developers
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information
# SPDX-License-Identifier: GPL-2.0

import grpc
from concurrent import futures
import time
import edf_databroker_train_pb2 as pb2
import edf_databroker_train_pb2_grpc as pb2_grpc
import os
from pathlib import Path

# gRPC port
port = 8061

data_path_rel = "tuh/"
edf_dirs: list = []


class EdfDatabroker(pb2_grpc.EdfDatabrokerServicer):
    def __init__(self):
        data_path_abs = os.environ['SHARED_FOLDER_PATH']
        data_path = f"{data_path_abs}/{data_path_rel}/"
        data_path_dev = f"{data_path}dev"
        for root, dirs, files in os.walk(data_path_dev):
            if len(dirs) == 0 and root.startswith(data_path):
                rel_path = root[len(data_path):]
                edf_dirs.append(rel_path)
        self.edf_dirs = edf_dirs

    def get_next_edf_dir(self, request, context):
        response = pb2.EdfDir()
        if len(self.edf_dirs) == 0:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("All data has been processed")
            sys.exit()
        else:
            response.dir = self.edf_dirs[0]
            self.edf_dirs.pop(0)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
pb2_grpc.add_EdfDatabrokerServicer_to_server(EdfDatabroker(), server)
print("Starting server. Listening on port : " + str(port))
server.add_insecure_port("[::]:{}".format(port))
server.start()

try:
    while True:
        time.sleep(86400)
except:
    server.stop(0)
