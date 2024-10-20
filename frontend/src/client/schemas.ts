export const $HTTPValidationError = {
	properties: {
		detail: {
			type: "array",
			contains: {
				type: "ValidationError",
			},
		},
	},
} as const;

export const $TodoCreate = {
	properties: {
		title: {
			type: "string",
			isRequired: true,
		},
		description: {
			type: "any-of",
			contains: [
				{
					type: "string",
				},
				{
					type: "null",
				},
			],
		},
		is_completed: {
			type: "boolean",
			default: false,
		},
	},
} as const;

export const $TodoRead = {
	properties: {
		id: {
			type: "number",
			isRequired: true,
		},
		title: {
			type: "string",
			isRequired: true,
		},
		description: {
			type: "any-of",
			contains: [
				{
					type: "string",
				},
				{
					type: "null",
				},
			],
		},
		is_completed: {
			type: "boolean",
			isRequired: true,
		},
	},
} as const;

export const $TodoUpdateSchema = {
	properties: {
		title: {
			type: "any-of",
			contains: [
				{
					type: "string",
				},
				{
					type: "null",
				},
			],
		},
		description: {
			type: "any-of",
			contains: [
				{
					type: "string",
				},
				{
					type: "null",
				},
			],
		},
		is_completed: {
			type: "any-of",
			contains: [
				{
					type: "boolean",
				},
				{
					type: "null",
				},
			],
		},
	},
} as const;

export const $ValidationError = {
	properties: {
		loc: {
			type: "array",
			contains: {
				type: "any-of",
				contains: [
					{
						type: "string",
					},
					{
						type: "number",
					},
				],
			},
			isRequired: true,
		},
		msg: {
			type: "string",
			isRequired: true,
		},
		type: {
			type: "string",
			isRequired: true,
		},
	},
} as const;
