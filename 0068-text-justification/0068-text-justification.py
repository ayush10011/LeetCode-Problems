class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0

        while i < len(words):
            # Find the words that fit in this line.
            j = i
            line_len = 0

            while j < len(words):
                # At least one space is needed between consecutive words.
                needed = line_len + len(words[j]) + (j - i)
                if needed > maxWidth:
                    break
                line_len += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_len

            # Last line or a line with only one word: left-justify.
            if j == len(words) or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                # Distribute spaces as evenly as possible.
                gaps = num_words - 1
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(num_words - 1):
                    line += words[i + k]
                    spaces = spaces_per_gap + (1 if k < extra_spaces else 0)
                    line += " " * spaces

                line += words[j - 1]
                res.append(line)

            i = j

        return res
        