# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0040-20261013-090848)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 27 | 415102 | 341760 | 82.3% | 83.2% |
| GLM 5.3 Flash | 37 | 491687 | 403200 | 82.0% | 83.0% |
| GPT-6.1 Sol | 28 | 664393 | 584704 | 88.0% | 89.7% |
| Sonnet 5.5 | 36 | 882148 | 837047 | 94.9% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9830 | 118603661 | 70276736 | 59.3% | 59.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1013 | 16534218 | 14638016 | 88.5% | 89.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8753 | 265083995 | 246948736 | 93.2% | 93.7% |
| Sonnet 5.5 | 8960 | 212217633 | 203088415 | 95.7% | 96.4% |
