# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0013-20261009-191602)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 180 | 2234208 | 1154688 | 51.7% | 51.6% |
| GPT-6.1 Sol | 91 | 2095049 | 1833216 | 87.5% | 88.1% |
| Sonnet 5.5 | 151 | 3499542 | 3355927 | 95.9% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3205 | 34584954 | 15875840 | 45.9% | 45.8% |
| GPT-6.1 Sol | 2841 | 83376446 | 77382272 | 92.8% | 93.3% |
| Sonnet 5.5 | 2977 | 66680810 | 63739854 | 95.6% | 96.2% |
