# matches = []
#     try:
#         for root, dirs, files in os.walk(os.getcwd()):
#             for file in files:
#                 full_path = os.path.join(root, file)
#                 if fragment in full_path:
#                     file_stats = os.stat(full_path)
#                     matches.append({
#                         "name": file,
#                         "path": full_path,
#                         "size": file_stats.st_size,
#                         "created": datetime.fromtimestamp(file_stats.st_birthtime).isoformat()
#                     })
#         return ORJSONResponse(status_code=200, content=matches)
#     except Exception as e:
#         return {"error": str(e)}, 500

import os
from datetime import datetime

def find_files(fragment, volume):
    matches = []
    try:
        for root, dirs, files in os.walk(volume):
            for file in files:
                full_path = os.path.join(root, file)
                if fragment in full_path:
                    file_stats = os.stat(full_path)
                    file_birthtime = file_stats.st_birthtime if os.name == 'nt' else file_stats.st_ctime
                    matches.append({
                        "volume": volume,
                        "name": file,
                        "path": full_path,
                        "size": file_stats.st_size,
                        "created": datetime.fromtimestamp(file_birthtime).isoformat()
                    })
        return matches
    except Exception as e:
        print(f"error: {e}")
        return "error"