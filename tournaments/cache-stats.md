# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0026-20261011-055315)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 78 | 822430 | 449536 | 54.7% | 54.6% |
| GPT-6.1 Sol | 58 | 1219646 | 1133568 | 92.9% | 93.9% |
| Sonnet 5.5 | 78 | 2127182 | 2048952 | 96.3% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6850 | 76656009 | 38613504 | 50.4% | 50.3% |
| GPT-6.1 Sol | 5410 | 155052759 | 144306304 | 93.1% | 93.5% |
| Sonnet 5.5 | 5729 | 126735363 | 121034761 | 95.5% | 96.1% |
