# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 95 | 811869 | 434560 | 53.5% | 53.8% |
| GPT-6.1 Sol | 111 | 2845780 | 2621056 | 92.1% | 92.9% |
| Sonnet 5.5 | 150 | 3628385 | 3482418 | 96.0% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2939 | 31496862 | 14270720 | 45.3% | 45.2% |
| GPT-6.1 Sol | 2673 | 79217105 | 73667328 | 93.0% | 93.4% |
| Sonnet 5.5 | 2743 | 61420600 | 58711155 | 95.6% | 96.2% |
