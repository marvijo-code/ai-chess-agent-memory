# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 51 | 948254 | 907776 | 95.7% | 96.4% |
| Fable 5.1 | 27 | 314334 | 287750 | 91.5% | 92.4% |
| GLM 5.3 Flash | 26 | 293535 | 270656 | 92.2% | 93.8% |
| GPT-6.1 Sol | 28 | 609161 | 541824 | 88.9% | 89.6% |
| Sonnet 5.5 | 27 | 577569 | 540786 | 93.6% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9147 | 105932321 | 58558592 | 55.3% | 55.3% |
| Fable 5.1 | 27 | 314334 | 287750 | 91.5% | 92.4% |
| GLM 5.3 Flash | 479 | 6799214 | 5990400 | 88.1% | 88.8% |
| GPT-6.1 Sol | 7864 | 234662787 | 218588416 | 93.2% | 93.6% |
| Sonnet 5.5 | 7864 | 178011409 | 170018846 | 95.5% | 96.2% |
