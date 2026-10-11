# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 124 | 1727822 | 1095680 | 63.4% | 63.5% |
| GPT-6.1 Sol | 65 | 1658224 | 1494912 | 90.2% | 91.5% |
| Sonnet 5.5 | 113 | 3389441 | 3270987 | 96.5% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8194 | 91662603 | 47252992 | 51.6% | 51.5% |
| GPT-6.1 Sol | 6536 | 190174884 | 177051264 | 93.1% | 93.6% |
| Sonnet 5.5 | 6647 | 145993254 | 139336127 | 95.4% | 96.1% |
