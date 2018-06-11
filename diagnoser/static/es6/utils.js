import _ from 'lodash';


const Utils = {
    buildUrl(args, query_string) {
        endpoint = 'api/' + args.join('/');

        if (query_string) {
            var endpoint = endpoint + '?';
            if (typeof(query_string) == 'string') {
                endpoint += '&' + query_string
            } else if (typeof(query_string) == 'object') {
                for (var key in query_string) {
                    var value = query_string[key];
                    endpoint += '&' + key + '=' + value
                }
            }
        }
        return endpoint
    }
};

export default Utils