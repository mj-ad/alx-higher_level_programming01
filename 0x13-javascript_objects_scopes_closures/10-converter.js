#!/usr/bin/node
exports.converter = function (base) {
    function con (number) {
	return number.toString(base);
    }
    return con;
};
