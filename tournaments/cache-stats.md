# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 126 | 5238581 | 4180480 | 79.8% | 80.1% |
| GLM 5.3 Flash | 203 | 9536312 | 7415808 | 77.8% | 78.0% |
| GPT-6.1 Sol | 316 | 13714663 | 13161216 | 96.0% | 96.5% |
| Haiku 5.5 | 182 | 7354304 | 6952266 | 94.5% | 95.0% |
| Sonnet 5.5 | 293 | 14229204 | 13285874 | 93.4% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10524 | 134881382 | 84368256 | 62.5% | 62.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1645 | 35071052 | 29894592 | 85.2% | 85.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9720 | 298402973 | 278080000 | 93.2% | 93.7% |
| Haiku 5.5 | 182 | 7354304 | 6952266 | 94.5% | 95.0% |
| Sonnet 5.5 | 10024 | 248926548 | 237921378 | 95.6% | 96.3% |
