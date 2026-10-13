# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0040-20261013-090848)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 45 | 639787 | 531840 | 83.1% | 85.2% |
| GLM 5.3 Flash | 37 | 491687 | 403200 | 82.0% | 83.0% |
| GPT-6.1 Sol | 44 | 956626 | 844800 | 88.3% | 90.8% |
| Sonnet 5.5 | 52 | 1141417 | 1072124 | 93.9% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9848 | 118828346 | 70466816 | 59.3% | 59.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1013 | 16534218 | 14638016 | 88.5% | 89.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8769 | 265376228 | 247208832 | 93.2% | 93.7% |
| Sonnet 5.5 | 8976 | 212476902 | 203323492 | 95.7% | 96.4% |
