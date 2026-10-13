# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0041-20261013-124210)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 232 | 5188355 | 4901760 | 94.5% | 95.1% |
| GLM 5.3 Flash | 185 | 4297643 | 3915264 | 91.1% | 91.7% |
| GPT-6.1 Sol | 233 | 6560544 | 5906176 | 90.0% | 90.7% |
| Sonnet 5.5 | 238 | 6662447 | 6335785 | 95.1% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10216 | 126295190 | 77374720 | 61.3% | 61.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1303 | 22458832 | 19816640 | 88.2% | 88.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9166 | 276783155 | 257553024 | 93.1% | 93.6% |
| Sonnet 5.5 | 9505 | 228506303 | 218716843 | 95.7% | 96.4% |
