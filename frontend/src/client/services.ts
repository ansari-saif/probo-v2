import type { CancelablePromise } from "./core/CancelablePromise";
import { OpenAPI } from "./core/OpenAPI";
import { request as __request } from "./core/request";

import type { TodoCreate, TodoRead, TodoUpdateSchema } from "./models";

export type DefaultData = {
	CreateTodoApiV1TodosPost: {
		requestBody: TodoCreate;
	};
	GetTodoApiV1TodosTodoIdGet: {
		todoId: number;
	};
	UpdateTodoApiV1TodosTodoIdPut: {
		requestBody: TodoUpdateSchema;
		todoId: number;
	};
	DeleteTodoApiV1TodosTodoIdDelete: {
		todoId: number;
	};
};

export class DefaultService {
	/**
	 * List All Todos
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static listAllTodosApiV1TodosGet(): CancelablePromise<
		Array<TodoRead>
	> {
		return __request(OpenAPI, {
			method: "GET",
			url: "/api/v1/todos/",
		});
	}

	/**
	 * Create Todo
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static createTodoApiV1TodosPost(
		data: DefaultData["CreateTodoApiV1TodosPost"],
	): CancelablePromise<TodoRead> {
		const { requestBody } = data;
		return __request(OpenAPI, {
			method: "POST",
			url: "/api/v1/todos/",
			body: requestBody,
			mediaType: "application/json",
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Todo
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static getTodoApiV1TodosTodoIdGet(
		data: DefaultData["GetTodoApiV1TodosTodoIdGet"],
	): CancelablePromise<TodoRead> {
		const { todoId } = data;
		return __request(OpenAPI, {
			method: "GET",
			url: "/api/v1/todos/{todo_id}",
			path: {
				todo_id: todoId,
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Todo
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static updateTodoApiV1TodosTodoIdPut(
		data: DefaultData["UpdateTodoApiV1TodosTodoIdPut"],
	): CancelablePromise<TodoRead> {
		const { todoId, requestBody } = data;
		return __request(OpenAPI, {
			method: "PUT",
			url: "/api/v1/todos/{todo_id}",
			path: {
				todo_id: todoId,
			},
			body: requestBody,
			mediaType: "application/json",
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Todo
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static deleteTodoApiV1TodosTodoIdDelete(
		data: DefaultData["DeleteTodoApiV1TodosTodoIdDelete"],
	): CancelablePromise<Record<string, unknown>> {
		const { todoId } = data;
		return __request(OpenAPI, {
			method: "DELETE",
			url: "/api/v1/todos/{todo_id}",
			path: {
				todo_id: todoId,
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}
}
