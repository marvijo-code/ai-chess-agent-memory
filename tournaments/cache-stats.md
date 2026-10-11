# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0027-20261011-075651)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 178 | 1858772 | 1028096 | 55.3% | 55.3% |
| GPT-6.1 Sol | 164 | 5045492 | 4654464 | 92.2% | 92.6% |
| Sonnet 5.5 | 167 | 3718853 | 3552731 | 95.5% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7222 | 80644234 | 40838144 | 50.6% | 50.6% |
| GPT-6.1 Sol | 5708 | 165199227 | 153777664 | 93.1% | 93.5% |
| Sonnet 5.5 | 5994 | 132151417 | 126177929 | 95.5% | 96.1% |
