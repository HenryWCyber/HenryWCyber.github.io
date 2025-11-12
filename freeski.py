import random
import binascii

class Mountain:
    def __init__(self, name, height, start_elev, start_horiz, encoded_flag):
        self.name = name
        self.height = height
        self.start_elev = start_elev
        self.start_horiz = start_horiz
        self.encoded_flag = encoded_flag
    
    def GetTreasureLocations(self):
        locations = {}
        random.seed(binascii.crc32(self.name.encode('utf-8')))
        prev_height = self.height
        prev_horiz = 0
        for i in range(0, 5):
            e_delta = random.randint(200, 800)
            h_delta = random.randint(int(0 - e_delta / 4), int(e_delta / 4))
            locations[prev_height - e_delta] = prev_horiz + h_delta
            prev_height = prev_height - e_delta
            prev_horiz = prev_horiz + h_delta
        return locations

def SetFlag(mountain, treasure_list):
    product = 0
    for treasure_val in treasure_list:
        product = product << 8 ^ treasure_val
    random.seed(product)
    decoded = []
    for i in range(0, len(mountain.encoded_flag)):
        r = random.randint(0, 255)
        decoded.append(chr(mountain.encoded_flag[i] ^ r))
    flag_text = 'Flag: %s' % ''.join(decoded)
    print(flag_text)

Mountains = [
    Mountain('Mount Snow', 3586, 3400, 2400, b'\x90\x00\x1d\xbc\x17b\xed6S"\xb0<Y\xd6\xce\x169\xae\xe9|\xe2Gs\xb7\xfdy\xcf5\x98'),
    Mountain('Aspen', 11211, 11000, 10000, b'U\xd7%x\xbfvj!\xfe\x9d\xb9\xc2\xd1k\x02y\x17\x9dK\x98\xf1\x92\x0f!\xf1\\\xa0\x1b\x0f'),
    Mountain('Whistler', 7156, 6000, 6500, b'\x1cN\x13\x1a\x97\xd4\xb2!\xf9\xf6\xd4#\xee\xebh\xecs.\x08M!hr9?\xde\x0c\x86\x02'),
    Mountain('Mount Baker', 10781, 9000, 6000, b'\xac\xf9#\xf4T\xf1%h\xbe3FI+h\r\x01V\xee\xc2C\x13\xf3\x97ef\xac\xe3z\x96'),
    Mountain('Mount Norquay', 6998, 6300, 3000, b'\x0c\x1c\xad!\xc6,\xec0\x0b+"\x9f@.\xc8\x13\xadb\x86\xea{\xfeS\xe0S\x85\x90\x03q'),
    Mountain('Mount Erciyes', 12848, 10000, 12000, b'n\xad\xb4l^I\xdb\xe1\xd0\x7f\x92\x92\x96\x1bq\xca`PvWg\x85\xb21^\x93F\x1a\xee'),
    Mountain('Dragonmount', 16282, 15500, 16000, b'Z\xf9\xdf\x7f_\x02\xd8\x89\x12\xd2\x11p\xb6\x96\x19\x05x))v\xc3\xecv\xf4\xe2\\\x9a\xbe\xb5')
]

def get_flag(mountain):
    locations = mountain.GetTreasureLocations()
    # Highest to lowest elevation
    treasure_list = [elev * 1000 + locations[elev] for elev in sorted(locations.keys(), reverse=True)]
    SetFlag(mountain, treasure_list)

if __name__ == "__main__":
    for mountain in Mountains:
        get_flag(mountain)
