# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0021-20261010-172846)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 196 | 2543117 | 1660928 | 65.3% | 65.3% |
| GPT-6.1 Sol | 127 | 3523959 | 3330304 | 94.5% | 94.8% |
| Sonnet 5.5 | 98 | 1773432 | 1667137 | 94.0% | 95.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5570 | 62200429 | 30448640 | 49.0% | 48.9% |
| GPT-6.1 Sol | 4558 | 132942553 | 123659776 | 93.0% | 93.5% |
| Sonnet 5.5 | 4779 | 106313678 | 101590650 | 95.6% | 96.1% |
