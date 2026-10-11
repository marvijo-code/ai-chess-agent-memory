# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 176 | 2402997 | 1516032 | 63.1% | 63.2% |
| GPT-6.1 Sol | 110 | 3056747 | 2760832 | 90.3% | 91.2% |
| Sonnet 5.5 | 157 | 4492094 | 4325162 | 96.3% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8246 | 92337778 | 47673344 | 51.6% | 51.6% |
| GPT-6.1 Sol | 6581 | 191573407 | 178317184 | 93.1% | 93.5% |
| Sonnet 5.5 | 6691 | 147095907 | 140390302 | 95.4% | 96.1% |
