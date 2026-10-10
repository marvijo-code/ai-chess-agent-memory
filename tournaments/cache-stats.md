# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 52 | 574542 | 250368 | 43.6% | 43.5% |
| GPT-6.1 Sol | 32 | 669866 | 607488 | 90.7% | 92.4% |
| Sonnet 5.5 | 63 | 1641850 | 1586639 | 96.6% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4554 | 50101978 | 23932544 | 47.8% | 47.7% |
| GPT-6.1 Sol | 3701 | 106035083 | 98381824 | 92.8% | 93.3% |
| Sonnet 5.5 | 3960 | 87412208 | 83487387 | 95.5% | 96.1% |
