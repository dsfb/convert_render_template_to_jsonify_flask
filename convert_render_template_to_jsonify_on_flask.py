


def get_substr_from(string, char):
	index = string.find(char)
	if index == -1:
		return ''
	else:
		return string[index:]


def remove_whitespaces(string):
    return string.strip()


def handle_tokens(token_str):
    work_tokens = token_str.split('=')
    if work_tokens[1].startswith('json.dumps('):
        work_tokens[1] = work_tokens[1][11:-1]
    work_tokens[0] = '\'' + work_tokens[0] + '\''
    return ': '.join(work_tokens)


def built_result_str(tokens):
    result = 'return jsonify({'
    for token in tokens:
        result += token + ', '
    return result[:-2] + '})'    


def is_html_param(param):
    return param.endswith('.html\'') or param.endswith('.html') or \
           param.endswith('.html"')


def convert_render_template_to_jsonify_on_flask(string):
    string = remove_whitespaces(string)
    params = get_substr_from(string, '(')[1:-1]
    param_tokens = []
    if params.find(', ') >= 0:
        param_tokens = params.split(', ')
    elif params.find(',\n') >= 0:
        param_tokens = params.split(',\n')[:-1]
        param_tokens = [token.strip() for token in param_tokens]
    selected = param_tokens[1:] if is_html_param(param_tokens[0]) else param_tokens
    results = []
    for tokens in selected:
        results.append(handle_tokens(tokens))

    print(built_result_str(results))

