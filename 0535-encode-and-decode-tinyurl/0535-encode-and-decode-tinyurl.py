class Codec:
    def __init__(self):
        self.map = {}      # short code -> long URL
        self.counter = 0   # increases by 1 each time encode() is called

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        code = str(self.counter)          # e.g. "1", "2", "3"...
        self.map[code] = longUrl          # remember what this code points to
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.split("/")[-1]    # grab just the code part after last "/"
        return self.map[code]             # look up original URL


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))