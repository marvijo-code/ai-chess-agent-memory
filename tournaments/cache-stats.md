# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 31 | 243884 | 108032 | 44.3% | 43.8% |
| GPT-6.1 Sol | 27 | 540923 | 478592 | 88.5% | 91.0% |
| Sonnet 5.5 | 18 | 210604 | 188976 | 89.7% | 92.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7602 | 85045091 | 43450880 | 51.1% | 51.0% |
| GPT-6.1 Sol | 6103 | 178030891 | 165889792 | 93.2% | 93.6% |
| Sonnet 5.5 | 6244 | 137125150 | 130898046 | 95.5% | 96.1% |
