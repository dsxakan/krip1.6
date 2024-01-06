import numpy as np

def sub_nibbles(state):
    # Пример замены байтов
    sbox = {
        0x00: 0x0c,
        0x01: 0x04,
        0x10: 0x0f,
        0x11: 0x07
    }
    # Применяем замену байтов из S-бокса
    return np.vectorize(lambda x: sbox.get(x, x))(state)

def shift_rows(state):
    # Пример сдвига строк
    # Сдвигаем каждую строку влево на количество позиций, равное номеру строки
    return np.roll(state, -1, axis=0)

def mix_columns(state):
    # Пример перемешивания столбцов
    mix_matrix = np.array([[2, 3], [1, 4]])
    # Перемножаем матрицу MixColumns на состояние
    # и берем остаток от деления на 16
    return np.dot(mix_matrix, state) % 16

def add_round_key(state, round_key):
    # Применяем операцию XOR к состоянию и раундовому ключу
    return state ^ round_key

def simplified_aes(input_text, round_key):
    # Преобразуем входные данные и раундовый ключ в матрицы 2x2
    state = np.array(input_text).reshape((2, 2))

    print("Input State:")
    print(state)

    round_key = np.array(round_key).reshape((2, 2))
    print("\nRound Key:")
    print(round_key)

    # Применяем операцию AddRoundKey
    state = add_round_key(state, round_key)
    print("\nAfter AddRoundKey:")
    print(state)

    # Применяем SubNibbles
    state = sub_nibbles(state)
    print("\nAfter SubNibbles:")
    print(state)

    # Применяем ShiftRows
    state = shift_rows(state)
    print("\nAfter ShiftRows:")
    print(state)

    # Применяем MixColumns
    state = mix_columns(state)
    print("\nAfter MixColumns:")
    print(state)

# Пример входных данных
input_text = [0x01, 0x23, 0x45, 0x67]
round_key = [0x89, 0xab, 0xcd, 0xef]

# Вызываем функцию для выполнения упрощенного AES первого раунда
simplified_aes(input_text, round_key)
