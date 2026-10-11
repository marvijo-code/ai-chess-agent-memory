# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0027-20261011-075651)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 178 | 1858772 | 1028096 | 55.3% | 55.3% |
| GPT-6.1 Sol | 180 | 5719765 | 5306624 | 92.8% | 93.1% |
| Sonnet 5.5 | 183 | 4251311 | 4074204 | 95.8% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7222 | 80644234 | 40838144 | 50.6% | 50.6% |
| GPT-6.1 Sol | 5724 | 165873500 | 154429824 | 93.1% | 93.6% |
| Sonnet 5.5 | 6010 | 132683875 | 126699402 | 95.5% | 96.1% |
