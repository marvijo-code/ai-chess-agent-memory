# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0035-20261012-085617)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 125 | 1981962 | 1823232 | 92.0% | 93.1% |
| GLM 5.3 Flash | 154 | 2133853 | 1839808 | 86.2% | 86.9% |
| GPT-6.1 Sol | 195 | 5786466 | 5379584 | 93.0% | 93.8% |
| Sonnet 5.5 | 222 | 5951656 | 5711141 | 96.0% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8856 | 100929984 | 53907840 | 53.4% | 53.4% |
| GLM 5.3 Flash | 288 | 3784493 | 3238848 | 85.6% | 86.3% |
| GPT-6.1 Sol | 7392 | 216729240 | 201730944 | 93.1% | 93.6% |
| Sonnet 5.5 | 7561 | 170173741 | 162522575 | 95.5% | 96.2% |
