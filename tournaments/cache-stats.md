# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 126 | 5238581 | 4180480 | 79.8% | 80.1% |
| GLM 5.3 Flash | 203 | 9536312 | 7415808 | 77.8% | 78.0% |
| GPT-6.1 Sol | 343 | 14373159 | 13764608 | 95.8% | 96.3% |
| Haiku 5.5 | 258 | 12047482 | 11485853 | 95.3% | 95.7% |
| Sonnet 5.5 | 367 | 18260779 | 17099211 | 93.6% | 94.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10524 | 134881382 | 84368256 | 62.5% | 62.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1645 | 35071052 | 29894592 | 85.2% | 85.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9747 | 299061469 | 278683392 | 93.2% | 93.7% |
| Haiku 5.5 | 258 | 12047482 | 11485853 | 95.3% | 95.7% |
| Sonnet 5.5 | 10098 | 252958123 | 241734715 | 95.6% | 96.3% |
