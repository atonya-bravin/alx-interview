def validUTF8(data) -> bool:
    index = 0

    def are_continuation_valid(start_index, num_bytes):
        return all(start_index < len(data) and (data[start_index] >> 6) == 0b10
                   for start_index in range(start_index, start_index + num_bytes))

    while index < len(data):
        if data[index] >> 7 == 0:  # Check for 1-byte character (0xxxxxxx)
            index += 1
        elif data[index] >> 5 == 0b110 and are_continuation_valid(index + 1, 1):  # Check for 2-byte character (110xxxxx 10xxxxxx)
            index += 2
        elif data[index] >> 4 == 0b1110 and are_continuation_valid(index + 1, 2):  # Check for 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            index += 3
        elif data[index] >> 3 == 0b11110 and are_continuation_valid(index + 1, 3):  # Check for 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
            index += 4
        else:
            return False

    return True
