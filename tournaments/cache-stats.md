# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0009-20261009-081556)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 23 | 158734 | 71680 | 45.2% | 44.4% |
| GPT-6.1 Sol | 47 | 1407867 | 1264128 | 89.8% | 90.5% |
| Sonnet 5.5 | 46 | 1037745 | 990367 | 95.4% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2283 | 25258084 | 11468032 | 45.4% | 45.3% |
| GPT-6.1 Sol | 1879 | 55040325 | 51277568 | 93.2% | 93.6% |
| Sonnet 5.5 | 2013 | 45631903 | 43656886 | 95.7% | 96.2% |
