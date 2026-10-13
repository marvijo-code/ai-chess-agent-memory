# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 34 | 525543 | 459008 | 87.3% | 88.0% |
| GLM 5.3 Flash | 28 | 337764 | 300800 | 89.1% | 90.8% |
| Sonnet 5.5 | 28 | 605035 | 568140 | 93.9% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9558 | 113121831 | 65179520 | 57.6% | 57.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 836 | 13392687 | 11845056 | 88.4% | 89.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8456 | 255741958 | 238279552 | 93.2% | 93.7% |
| Sonnet 5.5 | 8663 | 203278376 | 194473080 | 95.7% | 96.4% |
