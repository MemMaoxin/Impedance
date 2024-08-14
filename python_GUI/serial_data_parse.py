from constants import ALL_NAME_LIST, ALL_NAME_LIST_AS_ONE

DATASET_COUNT = 9
DATASET_SIZE = 2

def parse_package_data(data_bytes):
    parsed_data = {name: [] for name in ALL_NAME_LIST_AS_ONE}
    acupoint_number = data_bytes[1] - 0x30
    
    for dataset in range(DATASET_COUNT):
        ring_number = dataset % 3
        start_index = 2 + dataset * DATASET_SIZE
        acupoint_value = data_bytes[start_index] * 256 + data_bytes[start_index + 1]
        parsed_data[ALL_NAME_LIST[acupoint_number][ring_number]].append(acupoint_value)
    return parsed_data