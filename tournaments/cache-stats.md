# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0017-20261010-051708)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 67 | 1047430 | 834816 | 79.7% | 80.0% |
| GPT-6.1 Sol | 32 | 678702 | 612864 | 90.3% | 90.7% |
| Sonnet 5.5 | 32 | 515184 | 481123 | 93.4% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4214 | 46206753 | 22013184 | 47.6% | 47.6% |
| GPT-6.1 Sol | 3541 | 102215470 | 94923904 | 92.9% | 93.3% |
| Sonnet 5.5 | 3707 | 81583290 | 77897486 | 95.5% | 96.1% |
