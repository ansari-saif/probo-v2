export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};

export type TodoCreate = {
	title: string;
	description?: string | null;
	is_completed?: boolean;
};

export type TodoRead = {
	id: number;
	title: string;
	description?: string | null;
	is_completed: boolean;
};

export type TodoUpdateSchema = {
	title?: string | null;
	description?: string | null;
	is_completed?: boolean | null;
};

export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};
