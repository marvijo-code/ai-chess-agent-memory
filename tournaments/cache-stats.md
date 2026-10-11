# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0032-20261011-203427)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 55 | 694588 | 331776 | 47.8% | 47.3% |
| GPT-6.1 Sol | 26 | 557253 | 530048 | 95.1% | 96.4% |
| Sonnet 5.5 | 26 | 496553 | 465176 | 93.7% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8436 | 94755391 | 48880640 | 51.6% | 51.5% |
| GPT-6.1 Sol | 6770 | 198073230 | 184448512 | 93.1% | 93.6% |
| Sonnet 5.5 | 6804 | 149894737 | 143058973 | 95.4% | 96.1% |
