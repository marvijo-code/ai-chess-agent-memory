# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 51 | 948254 | 907776 | 95.7% | 96.4% |
| Fable 5.1 | 27 | 314334 | 287750 | 91.5% | 92.4% |
| GLM 5.3 Flash | 26 | 293535 | 270656 | 92.2% | 93.8% |
| GPT-6 Astra | 97 | 3976109 | 3844352 | 96.7% | 96.8% |
| GPT-6.1 Sol | 67 | 1629465 | 1469696 | 90.2% | 91.2% |
| Sonnet 5.5 | 66 | 1569041 | 1487453 | 94.8% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9147 | 105932321 | 58558592 | 55.3% | 55.3% |
| Fable 5.1 | 27 | 314334 | 287750 | 91.5% | 92.4% |
| GLM 5.3 Flash | 479 | 6799214 | 5990400 | 88.1% | 88.8% |
| GPT-6 Astra | 97 | 3976109 | 3844352 | 96.7% | 96.8% |
| GPT-6.1 Sol | 7903 | 235683091 | 219516288 | 93.1% | 93.6% |
| Sonnet 5.5 | 7903 | 179002881 | 170965513 | 95.5% | 96.2% |
